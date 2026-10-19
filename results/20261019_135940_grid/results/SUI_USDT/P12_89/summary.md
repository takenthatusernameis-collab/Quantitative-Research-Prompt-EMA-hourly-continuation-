# EMA Hourly Continuation — SUI/USDT P12_89

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6123 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.9263 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -4.9007 |
| sortino_ratio | -1.8591 |
| max_drawdown | 0.9025 |
| cagr | -0.5989 |
| net_avg_win | 41.4013 |
| net_avg_loss | -58.5665 |
| avg_hold_time_bars | 15.2517 |
| exposure | 0.5123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
