# EMA Hourly Continuation — AXL/USDT P12_34

**Symbol:** AXL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.6543 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -4.1045 |
| sortino_ratio | -1.5048 |
| max_drawdown | 0.8332 |
| cagr | -0.5007 |
| net_avg_win | 52.8501 |
| net_avg_loss | -63.9284 |
| avg_hold_time_bars | 6.7806 |
| exposure | 0.2056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
