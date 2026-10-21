# EMA Hourly Continuation — AXS/USDT P12_34

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7971 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.1051 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -1.6781 |
| sortino_ratio | -0.5754 |
| max_drawdown | 0.5063 |
| cagr | -0.2321 |
| net_avg_win | 64.0932 |
| net_avg_loss | -89.0808 |
| avg_hold_time_bars | 6.7937 |
| exposure | 0.1743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
