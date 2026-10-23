# EMA Hourly Continuation — KNC/USDT P100_144

**Symbol:** KNC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.5204 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 1.0158 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -4.3708 |
| sortino_ratio | -1.2934 |
| max_drawdown | 0.8060 |
| cagr | -0.4773 |
| net_avg_win | 39.8270 |
| net_avg_loss | -74.1660 |
| avg_hold_time_bars | 5.0652 |
| exposure | 0.1025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
