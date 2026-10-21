# EMA Hourly Continuation — ICP/USDT P8_20

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.9407 |
| net_win_rate | 0.5699 |
| gross_profit_factor | 1.3113 |
| gross_win_rate | 0.5699 |
| sharpe_ratio | -0.3456 |
| sortino_ratio | -0.1079 |
| max_drawdown | 0.2521 |
| cagr | -0.0543 |
| net_avg_win | 79.5256 |
| net_avg_loss | -112.0014 |
| avg_hold_time_bars | 5.4672 |
| exposure | 0.1138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
