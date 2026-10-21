# EMA Hourly Continuation — XCH/USDT P12_21

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.5641 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.7877 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -2.8240 |
| sortino_ratio | -0.6789 |
| max_drawdown | 0.5547 |
| cagr | -0.2689 |
| net_avg_win | 55.4845 |
| net_avg_loss | -79.5710 |
| avg_hold_time_bars | 5.2958 |
| exposure | 0.0684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
