# EMA Hourly Continuation — P2P/USDT P20_34

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.2482 |
| net_win_rate | 0.2996 |
| gross_profit_factor | 0.4595 |
| gross_win_rate | 0.3015 |
| sharpe_ratio | -12.6669 |
| sortino_ratio | -5.8470 |
| max_drawdown | 0.9994 |
| cagr | -0.9473 |
| net_avg_win | 10.4064 |
| net_avg_loss | -17.9388 |
| avg_hold_time_bars | 3.8242 |
| exposure | 0.1839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
