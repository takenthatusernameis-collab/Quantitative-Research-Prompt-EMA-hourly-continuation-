# EMA Hourly Continuation — ONT/USDT P55_144

**Symbol:** ONT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.5305 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8265 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.8021 |
| sortino_ratio | -1.1738 |
| max_drawdown | 0.7575 |
| cagr | -0.4276 |
| net_avg_win | 38.0993 |
| net_avg_loss | -62.8366 |
| avg_hold_time_bars | 12.3083 |
| exposure | 0.2673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
