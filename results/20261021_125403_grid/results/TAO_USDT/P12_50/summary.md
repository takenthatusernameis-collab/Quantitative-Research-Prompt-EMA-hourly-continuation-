# EMA Hourly Continuation — TAO/USDT P12_50

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9979 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.7742 |
| sortino_ratio | -0.6252 |
| max_drawdown | 0.5633 |
| cagr | -0.2517 |
| net_avg_win | 77.2556 |
| net_avg_loss | -92.3395 |
| avg_hold_time_bars | 10.6079 |
| exposure | 0.2927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
