# EMA Hourly Continuation — APE/USDT P12_144

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7998 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.2739 |
| sortino_ratio | -0.3300 |
| max_drawdown | 0.3354 |
| cagr | -0.1418 |
| net_avg_win | 79.1434 |
| net_avg_loss | -94.8283 |
| avg_hold_time_bars | 46.4742 |
| exposure | 0.6950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
