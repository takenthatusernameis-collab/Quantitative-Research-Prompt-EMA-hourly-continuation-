# EMA Hourly Continuation — XCH/USDT P12_26

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1624 |
| net_profit_factor | 0.2480 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.7129 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -12.9681 |
| sortino_ratio | -7.4370 |
| max_drawdown | 0.9999 |
| cagr | -0.9762 |
| net_avg_win | 5.0033 |
| net_avg_loss | -13.7786 |
| avg_hold_time_bars | 2.8288 |
| exposure | 0.2088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
