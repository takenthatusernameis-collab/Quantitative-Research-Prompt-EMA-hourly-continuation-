# EMA Hourly Continuation — DIA/USDT P50_144

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0491 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -2.4323 |
| sortino_ratio | -0.7844 |
| max_drawdown | 0.6341 |
| cagr | -0.3082 |
| net_avg_win | 51.0405 |
| net_avg_loss | -77.8946 |
| avg_hold_time_bars | 12.0618 |
| exposure | 0.2827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
