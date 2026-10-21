# EMA Hourly Continuation — ICP/USDT P12_20

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.8854 |
| net_win_rate | 0.5566 |
| gross_profit_factor | 1.2403 |
| gross_win_rate | 0.5566 |
| sharpe_ratio | -0.5134 |
| sortino_ratio | -0.1111 |
| max_drawdown | 0.1843 |
| cagr | -0.0513 |
| net_avg_win | 77.8304 |
| net_avg_loss | -110.3235 |
| avg_hold_time_bars | 3.8597 |
| exposure | 0.0388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
