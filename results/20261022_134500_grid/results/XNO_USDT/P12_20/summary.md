# EMA Hourly Continuation — XNO/USDT P12_20

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1624 |
| net_profit_factor | 0.2245 |
| net_win_rate | 0.3307 |
| gross_profit_factor | 0.6291 |
| gross_win_rate | 0.3590 |
| sharpe_ratio | -17.3450 |
| sortino_ratio | -10.0949 |
| max_drawdown | 1.0000 |
| cagr | -0.9949 |
| net_avg_win | 5.3918 |
| net_avg_loss | -11.8633 |
| avg_hold_time_bars | 2.1749 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
