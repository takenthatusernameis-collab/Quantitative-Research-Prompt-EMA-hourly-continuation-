# EMA Hourly Continuation — XMR/USDT P89_144

**Symbol:** XMR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.4969 |
| net_win_rate | 0.4054 |
| gross_profit_factor | 0.7002 |
| gross_win_rate | 0.4054 |
| sharpe_ratio | -3.5361 |
| sortino_ratio | -0.8093 |
| max_drawdown | 0.6112 |
| cagr | -0.3109 |
| net_avg_win | 57.1426 |
| net_avg_loss | -78.4102 |
| avg_hold_time_bars | 6.1120 |
| exposure | 0.0720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
