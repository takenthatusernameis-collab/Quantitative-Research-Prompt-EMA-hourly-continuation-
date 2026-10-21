# EMA Hourly Continuation — PUNDIX/USDT P12_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.7258 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -2.8863 |
| sortino_ratio | -0.9955 |
| max_drawdown | 0.7007 |
| cagr | -0.3681 |
| net_avg_win | 64.9100 |
| net_avg_loss | -81.2756 |
| avg_hold_time_bars | 19.5546 |
| exposure | 0.5209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
