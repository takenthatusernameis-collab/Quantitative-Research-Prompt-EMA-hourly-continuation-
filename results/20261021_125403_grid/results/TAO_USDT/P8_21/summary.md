# EMA Hourly Continuation — TAO/USDT P8_21

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.8760 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1264 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -0.8851 |
| sortino_ratio | -0.2730 |
| max_drawdown | 0.3773 |
| cagr | -0.1209 |
| net_avg_win | 80.7361 |
| net_avg_loss | -104.2227 |
| avg_hold_time_bars | 5.5811 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
