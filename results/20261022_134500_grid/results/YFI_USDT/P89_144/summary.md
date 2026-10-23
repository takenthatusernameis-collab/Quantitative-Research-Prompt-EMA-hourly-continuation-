# EMA Hourly Continuation — YFI/USDT P89_144

**Symbol:** YFI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -6.5205 |
| sortino_ratio | -2.1930 |
| max_drawdown | 0.9345 |
| cagr | -0.6550 |
| net_avg_win | 24.1981 |
| net_avg_loss | -47.1186 |
| avg_hold_time_bars | 5.7148 |
| exposure | 0.1451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
