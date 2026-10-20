# EMA Hourly Continuation — 1INCH/USDT P12_20

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1576 |
| net_profit_factor | 0.2246 |
| net_win_rate | 0.3775 |
| gross_profit_factor | 0.7171 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -15.7121 |
| sortino_ratio | -8.9893 |
| max_drawdown | 1.0000 |
| cagr | -0.9912 |
| net_avg_win | 4.8677 |
| net_avg_loss | -13.1460 |
| avg_hold_time_bars | 2.3027 |
| exposure | 0.1650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
