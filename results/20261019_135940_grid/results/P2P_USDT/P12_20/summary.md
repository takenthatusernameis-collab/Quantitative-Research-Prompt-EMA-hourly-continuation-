# EMA Hourly Continuation — P2P/USDT P12_20

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1406 |
| net_profit_factor | 0.2663 |
| net_win_rate | 0.2930 |
| gross_profit_factor | 0.5628 |
| gross_win_rate | 0.2980 |
| sharpe_ratio | -15.6792 |
| sortino_ratio | -8.3689 |
| max_drawdown | 1.0000 |
| cagr | -0.9864 |
| net_avg_win | 8.8092 |
| net_avg_loss | -13.7114 |
| avg_hold_time_bars | 2.8862 |
| exposure | 0.1845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
