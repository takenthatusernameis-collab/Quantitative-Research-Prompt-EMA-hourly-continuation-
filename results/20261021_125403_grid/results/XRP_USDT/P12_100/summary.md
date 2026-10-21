# EMA Hourly Continuation — XRP/USDT P12_100

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0236 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -1.7448 |
| sortino_ratio | -0.5368 |
| max_drawdown | 0.5247 |
| cagr | -0.2190 |
| net_avg_win | 63.5541 |
| net_avg_loss | -86.2661 |
| avg_hold_time_bars | 24.6652 |
| exposure | 0.5157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
