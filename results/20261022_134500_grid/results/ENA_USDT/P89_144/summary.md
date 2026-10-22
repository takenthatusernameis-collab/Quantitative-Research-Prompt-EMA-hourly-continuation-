# EMA Hourly Continuation — ENA/USDT P89_144

**Symbol:** ENA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6193 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.3100 |
| sortino_ratio | -0.9680 |
| max_drawdown | 0.7082 |
| cagr | -0.3751 |
| net_avg_win | 53.6829 |
| net_avg_loss | -80.5451 |
| avg_hold_time_bars | 4.6881 |
| exposure | 0.0929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
