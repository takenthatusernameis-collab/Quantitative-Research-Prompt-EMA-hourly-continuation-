# EMA Hourly Continuation — AXS/USDT P8_34

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1334 |
| net_profit_factor | 0.4922 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -8.0827 |
| sortino_ratio | -4.1304 |
| max_drawdown | 0.9943 |
| cagr | -0.8709 |
| net_avg_win | 15.5454 |
| net_avg_loss | -27.4244 |
| avg_hold_time_bars | 5.6589 |
| exposure | 0.3416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
