# EMA Hourly Continuation — STX/USDT P26_100

**Symbol:** STX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7375 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.8673 |
| sortino_ratio | -0.5547 |
| max_drawdown | 0.4991 |
| cagr | -0.2251 |
| net_avg_win | 63.1711 |
| net_avg_loss | -80.6891 |
| avg_hold_time_bars | 17.4161 |
| exposure | 0.3428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
