# EMA Hourly Continuation — SNX/USDT P34_89

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 1.0905 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -4.1479 |
| sortino_ratio | -1.5552 |
| max_drawdown | 0.8572 |
| cagr | -0.5331 |
| net_avg_win | 48.2147 |
| net_avg_loss | -70.7387 |
| avg_hold_time_bars | 7.1054 |
| exposure | 0.2318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
