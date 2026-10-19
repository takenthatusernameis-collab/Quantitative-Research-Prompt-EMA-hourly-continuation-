# EMA Hourly Continuation — STX/USDT P50_144

**Symbol:** STX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6564 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.6764 |
| sortino_ratio | -0.8005 |
| max_drawdown | 0.6284 |
| cagr | -0.3170 |
| net_avg_win | 52.4474 |
| net_avg_loss | -78.1704 |
| avg_hold_time_bars | 14.1978 |
| exposure | 0.2923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
