# EMA Hourly Continuation — ONE/USDT P12_20

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.8474 |
| net_win_rate | 0.5364 |
| gross_profit_factor | 1.1539 |
| gross_win_rate | 0.5402 |
| sharpe_ratio | -0.7753 |
| sortino_ratio | -0.1813 |
| max_drawdown | 0.2584 |
| cagr | -0.0809 |
| net_avg_win | 75.7487 |
| net_avg_loss | -103.4238 |
| avg_hold_time_bars | 4.5785 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
