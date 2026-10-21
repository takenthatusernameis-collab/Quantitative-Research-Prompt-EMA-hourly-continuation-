# EMA Hourly Continuation — GALA/USDT P21_55

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6971 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -2.7866 |
| sortino_ratio | -0.9151 |
| max_drawdown | 0.6769 |
| cagr | -0.3425 |
| net_avg_win | 60.1831 |
| net_avg_loss | -76.5019 |
| avg_hold_time_bars | 7.3566 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
