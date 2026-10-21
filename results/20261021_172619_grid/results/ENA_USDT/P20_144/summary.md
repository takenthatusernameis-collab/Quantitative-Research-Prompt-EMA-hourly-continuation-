# EMA Hourly Continuation — ENA/USDT P20_144

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.9206 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -0.4542 |
| sortino_ratio | -0.1278 |
| max_drawdown | 0.2268 |
| cagr | -0.0618 |
| net_avg_win | 87.1123 |
| net_avg_loss | -99.6807 |
| avg_hold_time_bars | 28.7031 |
| exposure | 0.5010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
