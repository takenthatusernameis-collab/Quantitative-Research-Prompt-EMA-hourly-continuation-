# EMA Hourly Continuation — WLD/USDT P20_34

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8009 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0343 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -1.1939 |
| sortino_ratio | -0.2860 |
| max_drawdown | 0.3339 |
| cagr | -0.1236 |
| net_avg_win | 80.4322 |
| net_avg_loss | -103.3595 |
| avg_hold_time_bars | 4.8921 |
| exposure | 0.0618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
