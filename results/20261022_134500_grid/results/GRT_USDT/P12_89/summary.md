# EMA Hourly Continuation — GRT/USDT P12_89

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.6280 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9326 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -4.6110 |
| sortino_ratio | -1.7204 |
| max_drawdown | 0.8837 |
| cagr | -0.5669 |
| net_avg_win | 44.6819 |
| net_avg_loss | -62.1657 |
| avg_hold_time_bars | 16.4930 |
| exposure | 0.5314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
