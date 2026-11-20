# EMA Hourly Continuation — P2P/USDT P20_100

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.3925 |
| gross_profit_factor | 0.6524 |
| gross_win_rate | 0.3941 |
| sharpe_ratio | -5.2931 |
| sortino_ratio | -1.8796 |
| max_drawdown | 0.8931 |
| cagr | -0.5886 |
| net_avg_win | 35.2820 |
| net_avg_loss | -45.6826 |
| avg_hold_time_bars | 13.8427 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
