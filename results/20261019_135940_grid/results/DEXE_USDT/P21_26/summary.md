# EMA Hourly Continuation — DEXE/USDT P21_26

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.1775 |
| net_win_rate | 0.3301 |
| gross_profit_factor | 0.6011 |
| gross_win_rate | 0.3837 |
| sharpe_ratio | -15.7387 |
| sortino_ratio | -8.1237 |
| max_drawdown | 1.0000 |
| cagr | -0.9876 |
| net_avg_win | 5.3147 |
| net_avg_loss | -14.7544 |
| avg_hold_time_bars | 3.5163 |
| exposure | 0.1966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
