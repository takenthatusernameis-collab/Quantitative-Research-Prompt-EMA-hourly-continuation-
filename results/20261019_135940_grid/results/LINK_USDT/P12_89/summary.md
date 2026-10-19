# EMA Hourly Continuation — LINK/USDT P12_89

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6445 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -4.6331 |
| sortino_ratio | -1.7099 |
| max_drawdown | 0.8826 |
| cagr | -0.5652 |
| net_avg_win | 48.7373 |
| net_avg_loss | -67.1766 |
| avg_hold_time_bars | 16.1342 |
| exposure | 0.5082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
