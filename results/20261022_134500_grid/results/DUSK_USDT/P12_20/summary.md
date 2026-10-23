# EMA Hourly Continuation — DUSK/USDT P12_20

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1426 |
| net_profit_factor | 0.3880 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.9250 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -10.3738 |
| sortino_ratio | -5.5171 |
| max_drawdown | 0.9991 |
| cagr | -0.9384 |
| net_avg_win | 10.0861 |
| net_avg_loss | -20.4573 |
| avg_hold_time_bars | 2.4516 |
| exposure | 0.1589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
