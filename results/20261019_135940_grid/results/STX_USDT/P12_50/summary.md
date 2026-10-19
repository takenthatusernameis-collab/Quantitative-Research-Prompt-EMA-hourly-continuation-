# EMA Hourly Continuation — STX/USDT P12_50

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1052 |
| net_profit_factor | 0.5093 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.8236 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -6.8480 |
| sortino_ratio | -3.1160 |
| max_drawdown | 0.9795 |
| cagr | -0.7803 |
| net_avg_win | 21.6915 |
| net_avg_loss | -34.1317 |
| avg_hold_time_bars | 7.5589 |
| exposure | 0.3598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
