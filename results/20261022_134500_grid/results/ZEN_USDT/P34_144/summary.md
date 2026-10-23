# EMA Hourly Continuation — ZEN/USDT P34_144

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6034 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.7115 |
| sortino_ratio | -1.1801 |
| max_drawdown | 0.7686 |
| cagr | -0.4273 |
| net_avg_win | 49.6259 |
| net_avg_loss | -68.3345 |
| avg_hold_time_bars | 18.5305 |
| exposure | 0.4287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
