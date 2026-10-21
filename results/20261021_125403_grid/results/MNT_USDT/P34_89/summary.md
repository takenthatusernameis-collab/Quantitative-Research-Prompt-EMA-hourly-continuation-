# EMA Hourly Continuation — MNT/USDT P34_89

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8451 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -3.0285 |
| sortino_ratio | -0.8741 |
| max_drawdown | 0.6512 |
| cagr | -0.3321 |
| net_avg_win | 50.0233 |
| net_avg_loss | -73.0509 |
| avg_hold_time_bars | 11.7579 |
| exposure | 0.2186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
