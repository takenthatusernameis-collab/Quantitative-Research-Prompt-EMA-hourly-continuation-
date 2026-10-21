# EMA Hourly Continuation — XDC/USDT P12_200

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7668 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0132 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.7010 |
| sortino_ratio | -0.4878 |
| max_drawdown | 0.4397 |
| cagr | -0.2012 |
| net_avg_win | 70.5123 |
| net_avg_loss | -92.4221 |
| avg_hold_time_bars | 33.3865 |
| exposure | 0.6085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
