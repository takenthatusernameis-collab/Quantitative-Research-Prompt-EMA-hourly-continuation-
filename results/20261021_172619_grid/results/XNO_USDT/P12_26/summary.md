# EMA Hourly Continuation — XNO/USDT P12_26

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.7691 |
| gross_win_rate | 0.4136 |
| sharpe_ratio | -4.4752 |
| sortino_ratio | -1.3597 |
| max_drawdown | 0.7984 |
| cagr | -0.4663 |
| net_avg_win | 51.6685 |
| net_avg_loss | -66.0431 |
| avg_hold_time_bars | 5.3260 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
