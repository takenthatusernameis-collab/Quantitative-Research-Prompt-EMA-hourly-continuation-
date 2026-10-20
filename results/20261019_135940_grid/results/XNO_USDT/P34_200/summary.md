# EMA Hourly Continuation — XNO/USDT P34_200

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.4889 |
| net_win_rate | 0.3961 |
| gross_profit_factor | 0.7065 |
| gross_win_rate | 0.3996 |
| sharpe_ratio | -5.7677 |
| sortino_ratio | -1.9338 |
| max_drawdown | 0.9033 |
| cagr | -0.6055 |
| net_avg_win | 38.3979 |
| net_avg_loss | -51.5224 |
| avg_hold_time_bars | 17.2165 |
| exposure | 0.4445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
