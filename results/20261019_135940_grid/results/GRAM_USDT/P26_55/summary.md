# EMA Hourly Continuation — GRAM/USDT P26_55

**Symbol:** GRAM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.3361 |
| net_win_rate | 0.4119 |
| gross_profit_factor | 0.7944 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -9.9066 |
| sortino_ratio | -4.3843 |
| max_drawdown | 0.9964 |
| cagr | -0.8919 |
| net_avg_win | 12.6095 |
| net_avg_loss | -26.2808 |
| avg_hold_time_bars | 3.9073 |
| exposure | 0.1725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
