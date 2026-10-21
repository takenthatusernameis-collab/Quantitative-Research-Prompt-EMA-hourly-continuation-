# EMA Hourly Continuation — STX/USDT P100_144

**Symbol:** STX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.8001 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0710 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -0.9427 |
| sortino_ratio | -0.2021 |
| max_drawdown | 0.2342 |
| cagr | -0.0889 |
| net_avg_win | 72.1899 |
| net_avg_loss | -98.7412 |
| avg_hold_time_bars | 7.4189 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
