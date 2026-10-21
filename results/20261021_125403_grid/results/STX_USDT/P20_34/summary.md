# EMA Hourly Continuation — STX/USDT P20_34

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7069 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7495 |
| sortino_ratio | -0.4385 |
| max_drawdown | 0.4482 |
| cagr | -0.1811 |
| net_avg_win | 62.4034 |
| net_avg_loss | -88.2726 |
| avg_hold_time_bars | 5.9641 |
| exposure | 0.0826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
