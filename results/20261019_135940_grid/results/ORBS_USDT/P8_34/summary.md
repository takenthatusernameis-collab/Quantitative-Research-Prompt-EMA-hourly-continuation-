# EMA Hourly Continuation — ORBS/USDT P8_34

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1344 |
| net_profit_factor | 0.3735 |
| net_win_rate | 0.3921 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -11.6651 |
| sortino_ratio | -6.0374 |
| max_drawdown | 0.9995 |
| cagr | -0.9515 |
| net_avg_win | 11.3060 |
| net_avg_loss | -19.5266 |
| avg_hold_time_bars | 6.6079 |
| exposure | 0.4037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
