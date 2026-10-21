# EMA Hourly Continuation — XMR/USDT P8_144

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7129 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.3645 |
| sortino_ratio | -0.7587 |
| max_drawdown | 0.6241 |
| cagr | -0.2945 |
| net_avg_win | 59.8898 |
| net_avg_loss | -76.7141 |
| avg_hold_time_bars | 26.6706 |
| exposure | 0.6146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
