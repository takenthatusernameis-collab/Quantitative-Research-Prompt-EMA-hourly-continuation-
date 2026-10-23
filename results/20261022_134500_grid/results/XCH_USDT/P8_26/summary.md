# EMA Hourly Continuation — XCH/USDT P8_26

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1825 |
| net_profit_factor | 0.2488 |
| net_win_rate | 0.4126 |
| gross_profit_factor | 0.6556 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -12.8367 |
| sortino_ratio | -7.7477 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 4.3991 |
| net_avg_loss | -12.4179 |
| avg_hold_time_bars | 3.3107 |
| exposure | 0.2746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
