# EMA Hourly Continuation — BSV/USDT P8_34

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1500 |
| net_profit_factor | 0.3908 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.8173 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -11.5036 |
| sortino_ratio | -6.2575 |
| max_drawdown | 0.9997 |
| cagr | -0.9579 |
| net_avg_win | 10.3450 |
| net_avg_loss | -18.6482 |
| avg_hold_time_bars | 5.0527 |
| exposure | 0.3445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
