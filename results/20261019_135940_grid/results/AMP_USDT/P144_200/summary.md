# EMA Hourly Continuation — AMP/USDT P144_200

**Symbol:** AMP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.3035 |
| net_win_rate | 0.3610 |
| gross_profit_factor | 0.6079 |
| gross_win_rate | 0.3738 |
| sharpe_ratio | -8.0459 |
| sortino_ratio | -2.6732 |
| max_drawdown | 0.9657 |
| cagr | -0.7380 |
| net_avg_win | 21.4638 |
| net_avg_loss | -39.9447 |
| avg_hold_time_bars | 4.7624 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
