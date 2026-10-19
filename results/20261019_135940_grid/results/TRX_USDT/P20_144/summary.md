# EMA Hourly Continuation — TRX/USDT P20_144

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.3635 |
| net_win_rate | 0.4037 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -7.3889 |
| sortino_ratio | -2.2915 |
| max_drawdown | 0.9558 |
| cagr | -0.7066 |
| net_avg_win | 27.9348 |
| net_avg_loss | -52.0403 |
| avg_hold_time_bars | 24.1159 |
| exposure | 0.5295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
