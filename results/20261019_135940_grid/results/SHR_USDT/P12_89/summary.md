# EMA Hourly Continuation — SHR/USDT P12_89

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.4720 |
| net_win_rate | 0.3479 |
| gross_profit_factor | 0.6489 |
| gross_win_rate | 0.3479 |
| sharpe_ratio | -9.4901 |
| sortino_ratio | -4.4622 |
| max_drawdown | 0.9958 |
| cagr | -0.8838 |
| net_avg_win | 22.3630 |
| net_avg_loss | -25.2770 |
| avg_hold_time_bars | 8.4790 |
| exposure | 0.4389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
