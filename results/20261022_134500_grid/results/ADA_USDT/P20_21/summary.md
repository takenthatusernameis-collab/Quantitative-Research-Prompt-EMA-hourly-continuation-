# EMA Hourly Continuation — ADA/USDT P20_21

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1190 |
| net_profit_factor | 0.0840 |
| net_win_rate | 0.2613 |
| gross_profit_factor | 0.5259 |
| gross_win_rate | 0.3454 |
| sharpe_ratio | -19.4145 |
| sortino_ratio | -10.5778 |
| max_drawdown | 1.0000 |
| cagr | -0.9976 |
| net_avg_win | 2.9495 |
| net_avg_loss | -12.4201 |
| avg_hold_time_bars | 1.4933 |
| exposure | 0.0808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
