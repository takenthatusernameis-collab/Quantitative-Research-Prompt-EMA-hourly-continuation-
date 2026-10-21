# EMA Hourly Continuation — MNT/USDT P26_144

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8767 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1087 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -0.6313 |
| sortino_ratio | -0.1647 |
| max_drawdown | 0.3099 |
| cagr | -0.0761 |
| net_avg_win | 73.6433 |
| net_avg_loss | -94.9083 |
| avg_hold_time_bars | 32.7134 |
| exposure | 0.4877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
