# EMA Hourly Continuation — SUI/USDT P12_200

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8413 |
| net_win_rate | 0.5245 |
| gross_profit_factor | 1.1035 |
| gross_win_rate | 0.5245 |
| sharpe_ratio | -0.9677 |
| sortino_ratio | -0.2495 |
| max_drawdown | 0.3628 |
| cagr | -0.1116 |
| net_avg_win | 79.6717 |
| net_avg_loss | -104.4770 |
| avg_hold_time_bars | 51.6074 |
| exposure | 0.7647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
