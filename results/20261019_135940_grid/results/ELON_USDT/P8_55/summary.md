# EMA Hourly Continuation — ELON/USDT P8_55

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1145 |
| net_profit_factor | 0.4898 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.7848 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -7.4887 |
| sortino_ratio | -3.5753 |
| max_drawdown | 0.9866 |
| cagr | -0.8200 |
| net_avg_win | 18.8254 |
| net_avg_loss | -30.1158 |
| avg_hold_time_bars | 8.4838 |
| exposure | 0.4415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
